from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b1f97b64-5ddc-5481-aa39-26520dabd2d5',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Glimmora.Name',
    display_name='Glimmora',
    searchable_by=['Glimmora', 'Stage 1', 'Glimmora'],
    subtypes=['Stage 1'],
    collector_number=126,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Glimmet.Name',
    family_id=969,
    abilities=[
        Ability(
            title='Shattering Crystal',
            game_text="When this Pokémon is Knocked Out, flip a coin. If heads, your opponent can't take any Prize cards for it.",
            effect=standard_ability,
            trigger=Triggers.ON_KNOCKED_OUT,
        ),
        Attack(
            title='Poison Petals',
            game_text="Your opponent's Active Pokémon is now Poisoned. During Pokémon Checkup, put 6 damage counters on that Pokémon instead of 1.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=standard_attack,
        ),
    ],
)
