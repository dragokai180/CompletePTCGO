from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b801718f-0f0e-5c70-98c0-cf4fe364e019',
    key='TwentiethAnn',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Slurpuff.Name',
    display_name='Slurpuff',
    searchable_by=['Slurpuff', 'Stage 1', 'Slurpuff'],
    subtypes=['Stage 1'],
    collector_number=120,
    set_code='TwentiethAnn',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Swirlix.Name',
    family_id=684,
    abilities=[
        Attack(
            title='Lap Up',
            game_text='Draw 3 cards.',
            cost={PokemonTypes.FAIRY: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Fairy Wind',
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
        ),
    ],
)
