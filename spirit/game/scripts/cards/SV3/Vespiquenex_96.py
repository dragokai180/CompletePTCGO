from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)
from spirit.game.card_effects.pokemon import TeraRulePassive


card = PokemonCardDef(
    guid='865f5fbe-f91f-560b-8dd4-6904e1389eac',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vespiquenex.Name',
    display_name='Vespiquen ex',
    searchable_by=['Vespiquen ex', 'Stage 1', 'ex', 'Tera', 'Vespiquenex'],
    subtypes=['Stage 1', 'ex', 'Tera'],
    collector_number=96,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Combee.Name',
    family_id=415,
    abilities=[
        Attack(
            title='Healing Pheromone',
            game_text='Heal 60 damage from 1 of your Pokémon.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Phantom Queen',
            game_text="Put 3 damage counters on each of your opponent's Benched Pokémon that has any damage counters on it.",
            cost={PokemonTypes.GRASS: 3},
            damage=200,
            effect=standard_attack,
        ),
    ],
    passive=TeraRulePassive(),
)
