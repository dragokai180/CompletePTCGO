from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fdbacd4c-c1aa-548b-ae06-022060a67687',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Blaziken.Name',
    display_name='Blaziken',
    searchable_by=['Blaziken', 'Stage 2', 'Blaziken'],
    subtypes=['Stage 2'],
    collector_number=14,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Combusken.Name',
    family_id=255,
    abilities=[
        Attack(
            title='Clutch',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
        Attack(
            title='Burning Shot',
            game_text="Discard 2 Energy attached to this Pokémon. This attack does 150 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
    ],
)
