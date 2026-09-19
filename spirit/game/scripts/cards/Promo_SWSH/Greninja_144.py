from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d6fa3a2b-ae72-549a-a85f-e4b238a02e28',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Greninja.Name',
    display_name='Greninja ★',
    searchable_by=['Greninja ★', 'Basic', 'Star', 'Greninja'],
    subtypes=['Basic', 'Star'],
    collector_number=144,
    set_code='Promo_SWSH',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH144'}},
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=658,
    abilities=[
        Ability(
            title='Shadow Knife',
            game_text="When you play this Pokémon from your hand onto your Bench during your turn, you may put 1 damage counter on 1 of your opponent's Pokémon.",
            ability_type=AbilityTypes.POKE_POWER,
            effect=standard_ability,
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title='Mist Slash',
            game_text="This attack's damage isn't affected by Weakness or Resistance, or by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
