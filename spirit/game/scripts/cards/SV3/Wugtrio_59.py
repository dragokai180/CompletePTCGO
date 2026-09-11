from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a611b2d0-8ddb-579c-83ca-ddb67e66cdaf',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wugtrio.Name',
    display_name='Wugtrio',
    searchable_by=['Wugtrio', 'Stage 1', 'Wugtrio'],
    subtypes=['Stage 1'],
    collector_number=59,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Wiglett.Name',
    family_id=960,
    abilities=[
        Attack(
            title='Entwining Entrapment',
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.WATER: 1},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
