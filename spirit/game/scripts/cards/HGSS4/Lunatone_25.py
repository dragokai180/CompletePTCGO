from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5f56bf14-6194-5ad0-a333-e8e59a6b43fd',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lunatone.Name',
    display_name='Lunatone',
    searchable_by=['Lunatone', 'Basic', 'Lunatone'],
    subtypes=['Basic'],
    collector_number=25,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=337,
    abilities=[
        Attack(
            title='Lunar Blast',
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
        Attack(
            title='Selfdestruct',
            game_text="Does 10 damage to each Benched Pokémon (both yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pokémon.) Lunatone does 60 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
