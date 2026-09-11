from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='85027375-1831-5026-bc93-71873e6f9832',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Umbreon.Name',
    display_name='Umbreon',
    searchable_by=['Umbreon', 'Stage 1', 'Umbreon'],
    subtypes=['Stage 1'],
    collector_number=96,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name',
    family_id=197,
    abilities=[
        Attack(
            title='Mach Claw',
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Lunatic Sense',
            game_text='Turn 1 of your face-down Prize cards face up. If that Prize card is a Pokémon, this attack does 60 more damage. (That Prize card remains up for the rest of the game.)',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
