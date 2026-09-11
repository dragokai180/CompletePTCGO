from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='16e2fad9-742c-557c-817d-c2b72523031b',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Krokorok.Name',
    display_name='Krokorok',
    searchable_by=['Krokorok', 'Stage 1', 'Krokorok'],
    subtypes=['Stage 1'],
    collector_number=84,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Sandile.Name',
    family_id=551,
    abilities=[
        Attack(
            title='Knock Off',
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Darkness Fang',
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
