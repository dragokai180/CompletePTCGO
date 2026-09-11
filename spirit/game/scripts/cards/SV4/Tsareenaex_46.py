from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)
from spirit.game.card_effects.pokemon import TeraRulePassive


card = PokemonCardDef(
    guid='67ecae0b-158c-52fd-ba2a-4a8dfbb2e380',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tsareenaex.Name',
    display_name='Tsareena ex',
    searchable_by=['Tsareena ex', 'Stage 2', 'Tera', 'ex', 'Tsareenaex'],
    subtypes=['Stage 2', 'Tera', 'ex'],
    collector_number=46,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=310,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Steenee.Name',
    family_id=761,
    abilities=[
        Attack(
            title='Icicle Sole',
            game_text="Put damage counters on 1 of your opponent's Pokémon until its remaining HP is 30.",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Trop Kick',
            game_text='Heal 30 damage from this Pokémon, and it recovers from all Special Conditions.',
            cost={PokemonTypes.GRASS: 2},
            damage=180,
            effect=standard_attack,
        ),
    ],
    passive=TeraRulePassive(),
)
