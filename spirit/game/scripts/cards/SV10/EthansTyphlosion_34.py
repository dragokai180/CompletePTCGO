from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="11f297bf-9261-5646-a2e9-fd2be59e110d",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EthansTyphlosion.Name",
    display_name="Ethan's Typhlosion",
    searchable_by=["Ethan's Typhlosion", "Stage 2", "EthansTyphlosion"],
    subtypes=["Stage 2"],
    collector_number=34,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.EthansQuilava.Name",
    family_id=155,
    abilities=[
        Attack(
            title="Buddy Blast",
            game_text="This attack does 60 more damage for each Ethan's Adventure card in your discard pile.",
            cost={PokemonTypes.FIRE: 1},
            damage=40,
            damage_operator="+",
            effect=standard_attack,
        ),
        Attack(
            title="Steam Artillery",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
        ),
    ],
)
