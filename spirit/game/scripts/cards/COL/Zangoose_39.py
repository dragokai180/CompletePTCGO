from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='da1a777f-e942-56da-a07c-fc05a088d4c1',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zangoose.Name',
    display_name='Zangoose',
    searchable_by=['Zangoose', 'Basic', 'Zangoose'],
    subtypes=['Basic'],
    collector_number=39,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=335,
    abilities=[
        Attack(
            title='Swords Dance',
            game_text="During your next turn, Zangoose's Lost Claw attack's base damage is 80.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Lost Claw',
            game_text="Choose 1 card from your opponent's hand without looking and put it in the Lost Zone.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
