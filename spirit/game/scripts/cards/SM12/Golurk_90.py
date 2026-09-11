from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='18ca5fa0-d9c5-51e3-b369-007cef785248',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Golurk.Name',
    display_name='Golurk',
    searchable_by=['Golurk', 'Stage 1', 'Golurk'],
    subtypes=['Stage 1'],
    collector_number=90,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Golett.Name',
    family_id=622,
    abilities=[
        Attack(
            title='Rock Tumble',
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Fist of Antiquity',
            game_text='If you have any Supporter cards in your discard pile, this attack does nothing.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=standard_attack,
        ),
    ],
)
