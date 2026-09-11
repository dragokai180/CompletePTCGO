from spirit.game.data_utils import Activations, PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.bw10 import shadow_punch, sinister_hand, sinister_hand_condition

card = PokemonCardDef(
    guid="d37bb8ee-217f-513d-a591-8e6e477f75b9",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dusknoir.Name",
    display_name="Dusknoir",
    searchable_by=["Dusknoir", "Stage 2", "Dusknoir"],
    subtypes=["Stage 2"],
    collector_number=104,
    set_code="BW10",
    rarity=Rarities.RareSecret,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dusclops.Name",
    family_id=477,
    abilities=[
        Ability(
            title="Sinister Hand",
            game_text="As often as you like during your turn (before your attack), you may move 1 damage counter from 1 of your opponent's Pok\u00e9mon to another of your opponent's Pok\u00e9mon.",
            effect=sinister_hand,
            activation=Activations.UNLIMITED,
            condition=sinister_hand_condition,
        ),
        Attack(
            title="Shadow Punch",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=shadow_punch,
        ),
    ],
)