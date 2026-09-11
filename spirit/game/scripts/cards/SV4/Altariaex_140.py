from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1a1252e9-6aa7-544d-99f8-503baa107dad',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Altariaex.Name',
    display_name='Altaria ex',
    searchable_by=['Altaria ex', 'Stage 1', 'ex', 'Altariaex'],
    subtypes=['Stage 1', 'ex'],
    collector_number=140,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name',
    family_id=333,
    abilities=[
        Ability(
            title='Humming Heal',
            game_text='Once during your turn, you may heal 20 damage from each of your Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Light Pulse',
            game_text="During your opponent's next turn, prevent all effects of attacks used by your opponent's Pokémon done to this Pokémon. (Damage is not an effect.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.METAL: 1},
            damage=140,
            effect=standard_attack,
        ),
    ],
)
