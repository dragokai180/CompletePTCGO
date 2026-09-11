from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e9086356-8b36-5a01-89e0-eda094726cd0',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gothorita.Name',
    display_name='Gothorita',
    searchable_by=['Gothorita', 'Stage 1', 'Gothorita'],
    subtypes=['Stage 1'],
    collector_number=40,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gothita.Name',
    family_id=574,
    abilities=[
        Attack(
            title='Fortunate Eye',
            game_text="Look at the top 5 cards of your opponent's deck and put them back on top of his or her deck in any order.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Smack',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
