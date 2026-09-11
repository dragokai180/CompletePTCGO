from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='83deb05d-b0ed-572c-ba17-46b7a1ebeab0',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ribombee.Name',
    display_name='Ribombee',
    searchable_by=['Ribombee', 'Stage 1', 'Ribombee'],
    subtypes=['Stage 1'],
    collector_number=93,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=60,
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
            title='Curative Pollen',
            game_text='Once during your turn (before your attack), you may heal 20 damage from 1 of your Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Fairy Wind',
            cost={PokemonTypes.FAIRY: 1},
            damage=30,
        ),
    ],
)
