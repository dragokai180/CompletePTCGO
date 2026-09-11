from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='854df758-8fc0-504c-8fa9-4a3b2013a2db',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pangoro.Name',
    display_name='Pangoro',
    searchable_by=['Pangoro', 'Stage 1', 'Pangoro'],
    subtypes=['Stage 1'],
    collector_number=82,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pancham.Name',
    family_id=674,
    abilities=[
        Attack(
            title='Sky Uppercut',
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=standard_attack,
        ),
        Attack(
            title='Magnum Punch',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 3},
            damage=130,
        ),
    ],
)
