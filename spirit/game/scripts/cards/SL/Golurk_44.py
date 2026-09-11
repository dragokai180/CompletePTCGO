from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7a77c183-cc76-5fc8-99c2-2f941a2b203e',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Golurk.Name',
    display_name='Golurk',
    searchable_by=['Golurk', 'Stage 1', 'Golurk'],
    subtypes=['Stage 1'],
    collector_number=44,
    set_code='SL',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
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
            title='Triple Smash',
            game_text='Flip 3 coins. This attack does 60 more damage for each heads.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Golurk Hammer',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
        ),
    ],
)
