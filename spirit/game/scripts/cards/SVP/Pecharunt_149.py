from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.session.passives import Passive


class ToxicSubjugationPassive(Passive):
    """While this Pokémon is Active, opponent's Poisoned Pokémon take 5 more
    damage counters during Pokémon Checkup."""

    def modify_poison_counters(self, counters, pokemon, carrier):
        if not is_in_active_spot(carrier):
            return counters
        if pokemon.owning_player_id == carrier.owning_player_id:
            return counters
        return counters + 5


card = PokemonCardDef(
    guid="edba2910-1eaf-5532-ba51-2a3e78bdd64b",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pecharunt.Name",
    display_name="Pecharunt",
    searchable_by=["Pecharunt","Basic","Pecharunt"],
    subtypes=["Basic"],
    collector_number=149,
    set_code="SVP",
    regulation_mark="H",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    family_id=1025,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    abilities=[
        Ability(
            title="Toxic Subjugation",
            game_text="As long as this Pokémon is in the Active Spot, put 5 more damage counters on your opponent's Poisoned Pokémon during Pokémon Checkup.",
            passive=ToxicSubjugationPassive(),
        ),
        Attack(
            title="Poison Chain",
            game_text="Your opponent's Active Pokémon is now Poisoned. During your opponent's next turn, that Pokémon can't retreat.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.POISONED, no_retreat=True),
        ),
    ],
)
