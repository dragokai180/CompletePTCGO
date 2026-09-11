from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ad819336-17bf-5795-aedb-bee4a428f1e1',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Orthworm.Name',
    display_name='Orthworm',
    searchable_by=['Orthworm', 'Basic', 'Orthworm'],
    subtypes=['Basic'],
    collector_number=151,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=968,
    abilities=[
        Ability(
            title='Nutritional Iron',
            game_text='If this Pokémon has 3 or more Metal Energy attached, it gets +100 HP.',
            passive=standard_passive('If this Pokémon has 3 or more Metal Energy attached, it gets +100 HP.'),
        ),
        Attack(
            title='Shoot Through',
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
