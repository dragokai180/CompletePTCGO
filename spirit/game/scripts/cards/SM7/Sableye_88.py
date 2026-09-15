from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3d0d3dcf-26c8-506e-9d89-a70a672c10ed',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sableye.Name',
    display_name='Sableye',
    searchable_by=['Sableye', 'Basic', 'Sableye'],
    subtypes=['Basic'],
    collector_number=88,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=302,
    abilities=[
        Ability(
            title='Excavate',
            game_text='Once during your turn (before your attack), you may look at the top card of your deck. You may discard that card.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Disable',
            game_text="Choose 1 of your opponent's Active Pokémon's attacks. That Pokémon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
            locks_next_turn=False,
        ),
    ],
)
