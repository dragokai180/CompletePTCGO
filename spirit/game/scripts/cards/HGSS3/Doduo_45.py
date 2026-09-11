from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0959c1c7-3172-5103-bd10-835d59231025',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Doduo.Name',
    display_name='Doduo',
    searchable_by=['Doduo', 'Basic', 'Doduo'],
    subtypes=['Basic'],
    collector_number=45,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=84,
    abilities=[
        Attack(
            title='Peck',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Double Headstrike',
            game_text='Flip 2 coins. If either of them is tails, this attack does nothing.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
