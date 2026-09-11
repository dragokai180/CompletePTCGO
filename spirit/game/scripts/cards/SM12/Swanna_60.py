from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='017676c2-938c-5547-b84e-aa6a23c3c696',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Swanna.Name',
    display_name='Swanna',
    searchable_by=['Swanna', 'Stage 1', 'Swanna'],
    subtypes=['Stage 1'],
    collector_number=60,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Ducklett.Name',
    family_id=580,
    abilities=[
        Attack(
            title='Tailwind',
            game_text='Attach an Energy card from your hand to 1 of your Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Air Slash',
            game_text='Discard an Energy from this Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
