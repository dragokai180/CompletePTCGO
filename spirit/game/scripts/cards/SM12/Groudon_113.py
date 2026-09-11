from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f4ff99db-4fb7-53ab-b766-6f6372b14eb3',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Groudon.Name',
    display_name='Groudon',
    searchable_by=['Groudon', 'Basic', 'Groudon'],
    subtypes=['Basic'],
    collector_number=113,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=383,
    abilities=[
        Attack(
            title='Drought',
            game_text='Attach up to 2 Fighting Energy cards from your hand to 1 of your Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Trembling Ground',
            game_text="This Pokémon can't use Trembling Ground during your next turn.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
