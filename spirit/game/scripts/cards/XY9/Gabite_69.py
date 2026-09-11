from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='243994c6-1144-5170-a2af-45cbb2a9467e',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gabite.Name',
    display_name='Gabite',
    searchable_by=['Gabite', 'Stage 1', 'Gabite'],
    subtypes=['Stage 1'],
    collector_number=69,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gible.Name',
    family_id=443,
    abilities=[
        Attack(
            title='Sand Tomb',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
