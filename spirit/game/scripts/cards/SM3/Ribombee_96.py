from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5eb538e9-6f74-5fae-bc56-ee138817a1bf',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ribombee.Name',
    display_name='Ribombee',
    searchable_by=['Ribombee', 'Stage 1', 'Ribombee'],
    subtypes=['Stage 1'],
    collector_number=96,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cutiefly.Name',
    family_id=742,
    abilities=[
        Ability(
            title='Honey Gather',
            game_text='Once during your turn (before your attack), you may search your deck for up to 2 basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Pollen Shot',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
