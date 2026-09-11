from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='265240b3-1dc6-50c8-bcf5-b14e43cc151c',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zapdos.Name',
    display_name='Zapdos',
    searchable_by=['Zapdos', 'Basic', 'Zapdos'],
    subtypes=['Basic'],
    collector_number=159,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=145,
    abilities=[
        Attack(
            title='Thunderous Assault',
            game_text="If this Pokémon was on the Bench and became your Active Pokémon this turn, this attack does 70 more damage. This attack's damage isn't affected by Weakness.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
