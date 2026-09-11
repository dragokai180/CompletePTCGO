from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='179f9233-8c5b-5fec-b916-5af4f8064d3e',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Magcargo.Name',
    display_name='Magcargo',
    searchable_by=['Magcargo', 'Stage 1', 'Magcargo'],
    subtypes=['Stage 1'],
    collector_number=27,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name',
    family_id=218,
    abilities=[
        Attack(
            title='Stomp Off',
            game_text="Discard the top 2 cards of your opponent's deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Flamethrower',
            game_text='Discard an Energy from this Pokémon.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
