from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6107b3da-3a4d-548b-9bfb-fcd31bd1a862',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name',
    display_name='Frogadier',
    searchable_by=['Frogadier', 'Stage 1', 'Frogadier'],
    subtypes=['Stage 1'],
    collector_number=40,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Froakie.Name',
    family_id=656,
    abilities=[
        Attack(
            title='Lick',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
