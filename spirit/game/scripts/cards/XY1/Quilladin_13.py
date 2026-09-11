from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5410daf9-f7f8-5125-891c-9bbdd44a9a71',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Quilladin.Name',
    display_name='Quilladin',
    searchable_by=['Quilladin', 'Stage 1', 'Quilladin'],
    subtypes=['Stage 1'],
    collector_number=13,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Chespin.Name',
    family_id=650,
    abilities=[
        Attack(
            title='Scrunch',
            game_text="Flip a coin. If heads, prevent all damage done to this Pokémon by attacks during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Wood Hammer',
            game_text='This Pokémon does 10 damage to itself.',
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
