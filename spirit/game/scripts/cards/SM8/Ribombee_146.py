from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='821b1215-ee09-5e3f-8738-7d64ddfdd0b0',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ribombee.Name',
    display_name='Ribombee',
    searchable_by=['Ribombee', 'Stage 1', 'Ribombee'],
    subtypes=['Stage 1'],
    collector_number=146,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cutiefly.Name',
    family_id=742,
    abilities=[
        Ability(
            title='Mysterious Buzz',
            game_text='As long as this Pokémon is on your Bench, whenever your opponent plays a Supporter card from their hand, prevent all effects of that card done to your Fairy Pokémon in play.',
            passive=standard_passive('As long as this Pokémon is on your Bench, whenever your opponent plays a Supporter card from their hand, prevent all effects of that card done to your Fairy Pokémon in play.'),
        ),
        Attack(
            title='Stampede',
            cost={PokemonTypes.FAIRY: 1},
            damage=20,
        ),
    ],
)
