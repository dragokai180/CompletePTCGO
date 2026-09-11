from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bee74dfa-3e5a-5857-9db8-eb294ecead8b',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vivillon.Name',
    display_name='Vivillon',
    searchable_by=['Vivillon', 'Stage 2', 'Vivillon'],
    subtypes=['Stage 2'],
    collector_number=137,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Spewpa.Name',
    family_id=666,
    abilities=[
        Attack(
            title='Dizzying Poison',
            game_text="Your opponent's Active Pokémon is now Confused and Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Powder',
            game_text="This attack does 30 more damage for each Fire Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
