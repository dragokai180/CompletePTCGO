from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8ddfec3c-156a-5d10-9ef1-1f2f0691f531',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gorebyss.Name',
    display_name='Gorebyss',
    searchable_by=['Gorebyss', 'Stage 1', 'Gorebyss'],
    subtypes=['Stage 1'],
    collector_number=43,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Clamperl.Name',
    family_id=366,
    abilities=[
        Attack(
            title='Deflecting Splash',
            game_text="During your opponent's next turn, prevent all damage done to this Pokémon by attacks from Evolution Pokémon.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
