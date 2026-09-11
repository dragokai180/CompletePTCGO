from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a393c054-37c0-5ef6-a8d1-6aa50b7840d5',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lickitung.Name',
    display_name='Lickitung',
    searchable_by=['Lickitung', 'Basic', 'Lickitung'],
    subtypes=['Basic'],
    collector_number=66,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=108,
    abilities=[
        Attack(
            title='Beat',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Tongue Whip',
            game_text="Choose 1 of your opponent's Benched Pokémon. This attack does 30 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=standard_attack,
        ),
    ],
)
