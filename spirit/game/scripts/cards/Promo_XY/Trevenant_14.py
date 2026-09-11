from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0a57343f-48a0-58bf-a049-ba60158b7c83',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Trevenant.Name',
    display_name='Trevenant',
    searchable_by=['Trevenant', 'Stage 1', 'Trevenant'],
    subtypes=['Stage 1'],
    collector_number=14,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Phantump.Name',
    family_id=709,
    abilities=[
        Attack(
            title='Eerie Wave',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Wood Hammer',
            game_text='Flip a coin. If tails, this Pokémon does 20 damage to itself.',
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
