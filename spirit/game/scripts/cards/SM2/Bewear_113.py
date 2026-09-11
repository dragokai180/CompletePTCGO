from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2502d43c-307b-54de-81f9-7ca610710184',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bewear.Name',
    display_name='Bewear',
    searchable_by=['Bewear', 'Stage 1', 'Bewear'],
    subtypes=['Stage 1'],
    collector_number=113,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Stufful.Name',
    family_id=759,
    abilities=[
        Ability(
            title='Rake It In',
            game_text='When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may draw 3 cards.',
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='Dangerous Blow',
            game_text="If your opponent's Active Pokémon is a Basic Pokémon, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
