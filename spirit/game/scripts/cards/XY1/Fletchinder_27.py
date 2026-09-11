from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a4e42d09-854e-5a43-85fa-3107ee2da79f',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Fletchinder.Name',
    display_name='Fletchinder',
    searchable_by=['Fletchinder', 'Stage 1', 'Fletchinder'],
    subtypes=['Stage 1'],
    collector_number=27,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Fletchling.Name',
    family_id=661,
    abilities=[
        Attack(
            title='Flame Charge',
            game_text='Search your deck for a Fire Energy card and attach it to this Pokémon. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Fire Wing',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
