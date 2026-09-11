from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)
from spirit.game.card_effects.pokemon import TeraRulePassive


card = PokemonCardDef(
    guid='5904b760-bf64-5ba0-a836-4e15f4654cf6',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Forretressex.Name',
    display_name='Forretress ex',
    searchable_by=['Forretress ex', 'Stage 1', 'Tera', 'ex', 'Forretressex'],
    subtypes=['Stage 1', 'Tera', 'ex'],
    collector_number=5,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pineco.Name',
    family_id=204,
    abilities=[
        Ability(
            title='Exploding Energy',
            game_text='Once during your turn, you may search your deck for up to 5 Basic Grass Energy cards and attach them to your Pokémon in any way you like. Then, shuffle your deck. If you searched your deck in this way, this Pokémon is Knocked Out.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Guard Press',
            game_text="During your opponent's next turn, this Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.GRASS: 2},
            damage=120,
            effect=standard_attack,
        ),
    ],
    passive=TeraRulePassive(),
)
