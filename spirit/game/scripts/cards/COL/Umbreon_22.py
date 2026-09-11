from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='883bcf65-29de-51b6-b2b9-fc75a9e73a45',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Umbreon.Name',
    display_name='Umbreon',
    searchable_by=['Umbreon', 'Stage 1', 'Umbreon'],
    subtypes=['Stage 1'],
    collector_number=22,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name',
    family_id=133,
    abilities=[
        Attack(
            title='Moonlight Fang',
            game_text="During your opponent's next turn, prevent all effects, including damage, done to Umbreon by attacks from your opponent's Pokémon than has any Poké-Powers or Poké-Bodies.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Quick Blow',
            game_text='Flip a coin. If heads, this attack does 30 damage plus 30 more damage.',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
