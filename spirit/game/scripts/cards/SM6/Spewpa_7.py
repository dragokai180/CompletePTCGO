from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6cc19852-0577-5247-a3a5-4c465aff4382',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Spewpa.Name',
    display_name='Spewpa',
    searchable_by=['Spewpa', 'Stage 1', 'Spewpa'],
    subtypes=['Stage 1'],
    collector_number=7,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Scatterbug.Name',
    family_id=664,
    abilities=[
        Attack(
            title='String Shot',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
