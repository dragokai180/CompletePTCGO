from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0f280013-bd05-549c-b845-877b55dcd80a',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cradily.Name',
    display_name='Cradily',
    searchable_by=['Cradily', 'Stage 2', 'Cradily'],
    subtypes=['Stage 2'],
    collector_number=11,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Lileep.Name',
    family_id=345,
    abilities=[
        Ability(
            title='Swaying Strangle',
            game_text="Your opponent's Pokémon that are affected by Special Conditions can't retreat.",
            passive=standard_passive("Your opponent's Pokémon that are affected by Special Conditions can't retreat."),
        ),
        Attack(
            title='Poison Tentacles',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
            effect=standard_attack,
        ),
    ],
)
