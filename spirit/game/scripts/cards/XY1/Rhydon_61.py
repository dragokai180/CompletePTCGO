from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='530587cf-3ea3-55e6-b9fd-35ca196a2001',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rhydon.Name',
    display_name='Rhydon',
    searchable_by=['Rhydon', 'Stage 1', 'Rhydon'],
    subtypes=['Stage 1'],
    collector_number=61,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Rhyhorn.Name',
    family_id=111,
    abilities=[
        Attack(
            title='Horn Drill',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title='Mad Mountain',
            game_text="Flip 2 coins. If both of them are heads, discard the top card of your opponent's deck for each damage counter on this Pokémon.",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
