from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='01d2903b-0b11-5505-bdc1-8dc2e965c4bf',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MAerodactylEX.Name',
    display_name='M Aerodactyl-EX',
    searchable_by=['M Aerodactyl-EX', 'MEGA', 'EX', 'MAerodactylEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=98,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.AerodactylEX.Name',
    family_id=142,
    abilities=[
        Attack(
            title='Rock Drill Dive',
            game_text="This attack does 10 damage to each Benched Pokémon (both yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
            effect=standard_attack,
        ),
    ],
)
