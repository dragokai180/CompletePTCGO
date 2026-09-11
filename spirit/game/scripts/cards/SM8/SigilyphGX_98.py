from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='843eb3fd-9494-5b8c-908a-6d19dab6fbe2',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.SigilyphGX.Name',
    display_name='Sigilyph-GX',
    searchable_by=['Sigilyph-GX', 'Basic', 'GX', 'SigilyphGX'],
    subtypes=['Basic', 'GX'],
    collector_number=98,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=561,
    abilities=[
        Ability(
            title='Mirror Counter',
            game_text="If this Pokémon is your Active Pokémon and is damaged by an attack from your opponent's Pokémon-GX or Pokémon-EX (even if this Pokémon is Knocked Out), put damage counters on the Attacking Pokémon equal to the damage done to this Pokémon.",
            effect=standard_ability,
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
        ),
        Attack(
            title='Sonic Wing',
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
        Attack(
            title='Intercept-GX',
            game_text="This attack does 60 damage times the amount of Energy attached to your opponent's Active Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='x',
            effect=standard_attack,
            gx=True,
        ),
    ],
)
