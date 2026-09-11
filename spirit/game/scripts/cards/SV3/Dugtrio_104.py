from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7a0789b1-4f4a-5947-b65c-84d8aa3d2f49',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dugtrio.Name',
    display_name='Dugtrio',
    searchable_by=['Dugtrio', 'Stage 1', 'Dugtrio'],
    subtypes=['Stage 1'],
    collector_number=104,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Diglett.Name',
    family_id=50,
    abilities=[
        Attack(
            title='Dig',
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
