from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4275097c-d457-5338-b6b4-69e008bf90d4',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Azumarill.Name',
    display_name='Azumarill',
    searchable_by=['Azumarill', 'Stage 1', 'Azumarill'],
    subtypes=['Stage 1'],
    collector_number=2,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name',
    family_id=183,
    abilities=[
        Attack(
            title='Waterfall',
            cost={PokemonTypes.WATER: 2},
            damage=40,
        ),
        Attack(
            title='Bubblebeam',
            game_text='Flip a coin. If heads, the Defending Pokémon is now Paralyzed.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
