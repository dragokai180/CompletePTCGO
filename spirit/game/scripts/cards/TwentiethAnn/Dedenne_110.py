from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5f77d765-f855-5fb3-aa4d-fa64d153b253',
    key='TwentiethAnn',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dedenne.Name',
    display_name='Dedenne',
    searchable_by=['Dedenne', 'Basic', 'Dedenne'],
    subtypes=['Basic'],
    collector_number=110,
    set_code='TwentiethAnn',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=702,
    abilities=[
        Attack(
            title='Rest',
            game_text='Heal 30 damage from this Pokémon. This Pokémon is now Asleep.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Pachi',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
