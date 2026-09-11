from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='aace7592-b5eb-511b-a649-0ab2ce351105',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mandibuzz.Name',
    display_name='Mandibuzz',
    searchable_by=['Mandibuzz', 'Stage 1', 'Mandibuzz'],
    subtypes=['Stage 1'],
    collector_number=93,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Vullaby.Name',
    family_id=629,
    abilities=[
        Attack(
            title='Trash Crash',
            game_text="Discard an Item card from your hand. If you do, this attack does 60 damage to 1 of your opponent's Pokémon. This damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Brave Bird',
            game_text='This Pokémon does 30 damage to itself.',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
